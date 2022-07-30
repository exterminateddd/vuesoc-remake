<template>
    <div class="form-container">
        <form class="login-form auth-form" autocomplete="off">
            <input type="text" name="login-form__username" id="username-for-login123" class="login-form__username" :placeholder="l('username')" v-model="usernameInput">
            <input type="password" name="login-form__password" id="password-for-login123" class="login-form__password" :placeholder="l('password')"  v-model="passwordInput">
            <input type="submit" :value="l('login')"  @click="onSubmit($event)">
        </form>
    </div>
</template>
<style scoped>
    @import url('../styles/LoginForm.css');
    @import url('../styles/AuthForm.css');
</style>
<script>
export default {
    name: 'LoginForm',
    inject: ['l'],
    data() {
        return {
            usernameInput: '',
            passwordInput: ''
        }
    },
    methods: {
        onSubmit(e) {
            e.preventDefault();
            let submittedData = {
                'username': this.usernameInput,
                'password': this.passwordInput
            };
            this.$props.loginAttemptHandler(submittedData);
        }
    },
    props: {
        loginAttemptHandler: {
            type: Function,
            required: true
        }
    }
}
</script>