<template>
    <div :class="{
            'sidebar__normal': !expanded,
            'sidebar__expanded': expanded
        }"
        @mouseover="setExpanded(true)" @mouseleave="setExpanded(false)"
        >
        <div class="top-section">
            <menu-element 
                v-for="el of menuElements" 
                v-bind:key="el" 
                :isExpanded="expanded" 
                :iconLink="el.iconLink" 
                :title="l(el.title)" 
                :targetLink="el.target">
            </menu-element>
            
            <select id="locale-select" v-model="selectedLocale">
                <option value="EN">EN</option>
                <option value="RU">RU</option>
            </select>
        </div>
        
        <div class="bottom-section">
            <menu-element 
                v-for="el of menuElementsStickedToBottom" 
                v-bind:key="el" :isExpanded="expanded" 
                :iconLink="el.iconLink" 
                :title="l(el.title)" 
                :targetLink="el.target">
            </menu-element>
        </div>
    </div>
</template>
<style scoped>
@import url("../styles/SidebarMenu.css");
</style>
<script>
import MenuElement from '@/components/MenuElement.vue';
export default {
    name: 'SidebarMenu',
    data() {
        return {
            expanded: false,
            menuElements: [
                {
                    "title": 'home',
                    "iconLink": require("@/assets/home-32.svg"),
                    "target": "/"
                }
            ],
            menuElementsStickedToBottom: [
                {
                    "title": 'auth',
                    "iconLink": require("@/assets/login-32.svg"),
                    "target": "/auth"
                },
                {
                    "title": 'logout',
                    "iconLink": require("@/assets/logout-32.svg"),
                    "target": "/logout"
                }
            ],
            selectedLocale: 'EN'
        }
    },
    inject: ['l'],
    methods: {
        setExpanded(v) {
            this.expanded = v;
        }
    },
    components: {
        MenuElement
    },
    watch: {
        selectedLocale(newLocale) {
            this.$props.localeChangeHandler(newLocale);
        }
    },
    created() {
        this.selectedLocale = this.$store.state.locale;
    },
    props: {
        localeChangeHandler: {
            type: Function,
            required: true
        }
    }
}
</script>