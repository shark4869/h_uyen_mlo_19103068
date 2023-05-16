import { updateUser, updateAvatar } from "./PersonalSlice";
import axios from "axios";

export const editUser = (userId, infor) => async dispatch => {
  try {
    const token = localStorage.getItem('token');
    const config = {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    };
    const response = await axios.put(`http://127.0.0.1:5000/api/user/${userId}`, infor, config);
    dispatch(updateUser(response.data.user));
    // console.log('check mesage: ', response.data)
  } catch (e) {
    console.log("error: ", e.message);
  }
};

export const editAvatar = (id, avatar) => async dispatch => {
  try {
    const token = localStorage.getItem('token');
    const config = {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    };
    const response = await axios.put(`http://127.0.0.1:5000/api/user/avatar/${id}`, avatar, config);
    dispatch(updateAvatar(response.data.user));
    console.log('check mesage: ', response.data)
  } catch (e) {
    console.log("error: ", e.message);
  }
};
// export const fetchRoles = () => async dispatch => {
//   try {
//     const response = await axios.get('http://localhost:3001/api/roles');
//     dispatch(getRoles(response.data));
//     // console.log("user data: ",response.data );
//   } catch (error) {
//     throw error;
//   }
// };