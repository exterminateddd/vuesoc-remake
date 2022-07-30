<template>
    <img src="../assets/spinner-32.svg" alt="" :class="{'hide': !keepSpinning, 'spinner': true}">
</template>
<style scoped>
.spinner {
    display: block;
    width: 48px;
    height: 48px;
    animation: spin 1s linear infinite;
}
.hide {
    display: none;
}
</style>
<script>
export default {
    name: 'Spinner',
    data() {
        return {

        }
    },
    props: {
        'keepSpinning': {
            'type': Boolean,
            'required': 'true'
        }
    }
}
</script>