import AuthSvc from "../services/auth.service.js";

let storedUser = localStorage.getItem('currentUser');
let storedLocation = localStorage.getItem('location');
let storedToken = localStorage.getItem('authToken');

let initialState = {
    "user": storedUser ? {"username": storedUser} : {},
    "location": storedLocation | {},
    "token": storedToken,
    "loggedIn": !!storedUser
};

let AuthSvcInstance = new AuthSvc();

AuthSvcInstance.setAuthToken(storedToken);

export const auth = {
    state: () => (initialState),
    namespaced: true,
    actions: {
        loginByUsername({commit}, {username, password, successCallback, errorCallback}) {
            AuthSvcInstance.loginByUsername(username, password)
                .then((response) => {
                    if (response.data.success) {
                        commit('loginSuccess', {'username': username, 'token': response.data.data.access_token});
                        successCallback();
                    } else {
                        throw new Error(response.data.errors[0]);
                    }
                })
                .catch((error) => {
                    errorCallback(error.message);
                })
        },
        loginByEmail() {

        },
        updateUserData({commit}) {
            AuthSvcInstance.getCurrentUser()
                .then((response) => {
                    console.log(response);
                    commit('userUpdate', response.data.data);
                })
                .catch((error) => {
                    console.log(400 <= error.response.status < 500)
                })
        },
        logout({commit}, {successCallback}) {
            AuthSvcInstance.logout()
                .then((response) => {
                    console.log(response.data, "OUTTTT");
                    successCallback();
                    commit('logoutSuccess');
                })
        }
    },
    mutations: {
        loginSuccess(state, payload) {
            this.commit('auth/userUpdate', {'username': payload.username});
            this.commit('auth/setAuthToken', payload.token);
            this.state.loggedIn = true;
        },
        logoutSuccess() {
            this.commit('auth/userUpdate', {});
            this.commit('auth/setAuthToken', "");
            this.state.loggedIn = false;
        },
        userUpdate(state, payload) {
            state.user = payload;
            localStorage.setItem('currentUser', payload.username);
        },
        setAuthToken(state, newToken) {
            state.token = newToken;
            localStorage.setItem('authToken', newToken);
            AuthSvcInstance.setAuthToken(newToken);
        }
    }
}
