import axios from 'axios';

const API_URL = 'http://192.168.0.101:5050/';
const axiosInstance = axios.create();

export default class AuthSvc {
    loginByUsername(username, password) {
        return new Promise((res, rej) => {
            axiosInstance.post(API_URL + 'auth/login', {
                'mode': 'username',
                'user_data': {
                    'username': username,
                    'password': password
                }
            }
            ).then((response) => {
                res(response);
            }).catch((err) => {
                rej(err);
            })
        })
    }
    loginByEmail(email, password) {
        return new Promise((res, rej) => {
            axiosInstance.post(API_URL + 'auth/login', {
                mode: 'email',
                user_data: {
                    'email': email,
                    'password': password
                }
            }).then((response) => {
                res(response);
            }).catch((err) => {
                rej(err);
            })
        })
    }
    logout() {
        return new Promise((res, rej) => {
            axiosInstance.post(API_URL + 'auth/logout', {})
                .then((response) => {
                    res(response);
                })
                .catch((err) => {
                    rej(err);
                })
        })
    }
    getCurrentUser() {
        return new Promise((res, rej) => {
            axiosInstance.get(API_URL + 'auth/current_user')
                .then((response) => {
                    res(response);
                })
                .catch((err) => {
                    rej(err);
                })
        })
    }
    setAuthToken(newToken) {
        this.token = newToken;
        axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${this.token ? this.token : "NoAuthorizationToday"}`;
    }
}
