<template>
    <div class="form-container">
        <form class="register-form auth-form" autocomplete="do-not-autofill"> 
            <input type="text" name="register-form__username" id="" class="register-form__username" :placeholder="l('username')" autocomplete="do-not-autofill">
            <input type="password" name="register-form__password" id="" class="register-form__password" :placeholder="l('password')" autocomplete="do-not-autofill">
            <input type="password" name="register-form__password-repeat" id="" class="register-form__password-repeat" :placeholder="l('password')" autocomplete="do-not-autofill">
            <input type="submit" :value="l('login')">
        </form>
    </div>
</template>
<style scoped>
    @import url('../styles/RegistrationForm.css');
    @import url('../styles/AuthForm.css');
</style>
<script>
export default {
    name: 'RegistrationForm',
    inject: ['l']
}
</script>