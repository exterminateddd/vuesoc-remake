<template>
    <div class="container auth-container">
        <div class="container-top">
        </div>
        <div class="container-center">
            <div class="container-info-section">
                {{$store.state.auth.user.username}}
                <device-info></device-info>
            </div>
            <div class="auth-form-container">
                <div class="action-select">
                    <input class="action-input" value="login" v-model="authAction" type="radio" id="login"/>
                    <label for="login" class="action-label">{{l('login')}}</label>

                    <input class="action-input" value="register" v-model="authAction" type="radio" id="register"/>
                    <label for="register" class="action-label">{{l('register')}}</label>
                </div>

                <div :class="{
                        'spinner-section': true,
                        'hide': !isLoading
                    }">
                    <spinner :keepSpinning="isLoading"></spinner>
                </div>

                <login-form v-if="authAction==='login'" :loginAttemptHandler="attemptLogin">
                </login-form>

                <registration-form v-if="authAction==='register'">
                </registration-form>
            </div>
        </div>
        <div class="container-bottom">
            
        </div>
    </div>
</template>
<style scoped>
@import url('../styles/AuthenticationView.css');
</style>
<script>
import RegistrationForm from '@/components/RegistrationForm.vue';
import LoginForm from '@/components/LoginForm.vue';
import DeviceInfo from '@/components/DeviceInfo.vue';
import Spinner from '@/components/Spinner.vue';

export default {
    name: 'AuthenticationView',
    data() {
        return {
            authAction: 'login',
            isLoading: false
        }
    },
    methods: {
        attemptLogin(loginData) {
            this.isLoading = true;

            let loginPayload = loginData;
            loginPayload.successCallback = this.onLoginSuccess;
            loginPayload.errorCallback = this.onLoginError;
            this.$store.dispatch('auth/loginByUsername', loginPayload);
        },
        onLoginSuccess() {
            this.isLoading = false;
            console.log("SUCCESS!!!");
        },
        onLoginError(error) {
            console.log("ERROR!!!", this.l(error));
        }
    },
    inject: ['l'],
    components: {
        RegistrationForm,
        LoginForm,
        DeviceInfo,
        Spinner
    }
}
</script>