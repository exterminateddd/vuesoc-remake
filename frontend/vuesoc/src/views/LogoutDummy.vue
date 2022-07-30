<template>
    <div class="container logout-container">
        <div class="logout-form">
            wanna log out fr??
            <button class="logout-confirm-btn" @click="attemptLogout()">
                Proceed to log out
            </button>
        </div>
    </div>
</template>
<style scoped>
    @import url("../styles/LogoutDummy.css");
</style>
<script>
export default {
    name: 'LogoutDummy',
    methods: {
        attemptLogout() {
            this.$store.dispatch('auth/logout', {
                "successCallback": this.redirectToHome
            })
        },
        redirectToHome() {
            this.$router.push({path: "/"})
        }
    }
}
</script>