from app.extentions import db
from app.app_ma import ServiceSchema
from app.model import Services, Categories
from flask import request, jsonify
import json
import os


service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)

# POST


def add_service_cleaning():
    data = request.json
    if (data and ('name' in data) and ('category_id' in data) and ('description' in data) and ('employee_id' in data) and ('price' in data)):
        name = data['name']
        category_id = data['category_id']
        description = data['description']
        employee_id = data['employee_id']
        price = data['price']
        try:
            new_service = Services(
                name, category_id, description, employee_id, price, is_deleted=False)
            db.session.add(new_service)
            db.session.commit()
            response = {
            'message': "Add service successfully",
            'service': {
                'id': new_service.id,
                'name': new_service.name,
                'category_id': new_service.category_id,
                'description': new_service.description,
                'employee_id': new_service.employee_id,
                'price': new_service.price,
                'is_deleted': new_service.is_deleted
                }
            }
            return jsonify(response), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({'message': 'Can not add service'}), 403

# GET


def get_service_by_id_service(id):
    service = Services.query.get(id)
    if service:
        return service_schema.jsonify(service)
    else:
        return jsonify({'message': 'Not found service'}), 404


def get_service_by_category_service(category_id):
    services = Services.query.join(Categories).filter(
        Categories.id == category_id).all()
    if services:
        return services_schema.jsonify(services)
    else:
        return jsonify({'message': 'Not found service'}), 404


def get_all_services_service():
    services = Services.query.all()
    if services:
        return services_schema.jsonify(services)
    else:
        return jsonify({'message': 'Not found service'}), 404

# UPDATE


def update_service_by_id_service(id):
    service = Services.query.get(id)
    if service:
        try:
            data = request.json
            if data:
                if "name" in data:
                    service.name = data["name"]
                if "category_id" in data:
                    service.category_id = data["category_id"]
                if "description" in data:
                    service.description = data["description"]
                if "employee_id" in data:
                    service.employee_id = data["employee_id"]
                if "price" in data:
                    service.price = data["price"]
            db.session.commit()
            response = {
            'message': "Update service successfully",
            'service': {
                'id': service.id,
                'name': service.name,
                'category_id': service.category_id,
                'description': service.description,
                'employee_id': service.employee_id,
                'price': service.price,
                'is_deleted': service.is_deleted,
                }
            }
            return jsonify(response), 200
        except:
            db.session.rollback()
            return jsonify({'message': 'Can not update service'}), 403
    else:
        return jsonify({'message': 'Service not found'}), 404


# delete


def delete_service_by_id_service(id):
    service = Services.query.get(id)
    if service:
        try:
            # db.session.delete(service)
            service.is_deleted = True  # Đánh dấu sản phẩm là đã bị xóa
            db.session.commit()
            return jsonify({'message': 'Delete service successfully'}), 200
        except Exception as e:
            db.session.rollback()
            error_message = str(e)
            return jsonify({'message': 'Can not delete service', 'error': error_message}), 403
    else:
        return jsonify({'message': 'Not found service'}), 404

#restore 
def restore_service_by_id_service(id):
    service = Services.query.get(id)
    if service:
        try:
            service.is_deleted = False  # Đánh dấu sản phẩm là đã bị xóa
            db.session.commit()
            return jsonify({'message': 'Restore service successfully'}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({'message': 'Can not delete service'}), 400
    else:
        return jsonify({'message': 'Not found restore'}), 404