<template>
    <router-link :to="target" :class='{
            "link__disabled": disabled,
            "link__active": shouldBeActive
        }'>
        <slot/>
    </router-link>
</template>
<style scoped>
    @import "../styles/MenuRouteLink.css";
</style>
<script>
export default {
    computed: {
        shouldBeActive() {
            return this.$root.$router.path===this.target | this.active;
        }
    },
    props: {
        'disabled': {
            type: Boolean,
            default: false,
            required: false
        },
        'active': {
            type: Boolean,
            default: false,
            required: false
        },
        'target': {
            type: String,
            required: true
        }
    }
}
</script>