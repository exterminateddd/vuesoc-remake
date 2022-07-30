<template>
    <div :class='{
        "menu-element__normal": !isExpanded,
        "menu-element__expanded": isExpanded
    }'>
        <div class="hero-section">
            <img :src="iconLink" alt="icon" @click="goToTarget()">
        </div>
        <div class="expanded-section">
            <menu-route-link :target="targetLink">{{title}}</menu-route-link>
        </div>
    </div>
</template>
<style scoped>
@import url(../styles/MenuElement.css);
</style>
<script>
import MenuRouteLink from '@/components/MenuRouteLink.vue';
export default {
    name: 'MenuElement',
    components: {
        MenuRouteLink
    },
    methods: {
        goToTarget() {
           this.$router.push({'path': this.targetLink});
        }
    },
    props: {
        'isExpanded': {
            type: Boolean,
            required: false,
            default: false
        },
        'iconLink': {
            type: String,
            required: true
        },
        'targetLink': {
            type: String,
            required: true
        },
        'title': {
            type: String,
            required: true
        } 
    }
}
</script>