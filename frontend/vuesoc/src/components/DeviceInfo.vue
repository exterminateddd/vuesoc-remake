<template>
    <div class="info-container">
        <div class="time-section">
            <h1>{{timeString}}</h1>
        </div>
        <div class="location-section">
            <spinner :keepSpinning="isLoading"></spinner>
            <div :class="{'hide': isLoading, 'location': true}">
                <img src="../assets/location-32.svg" alt=""> <h1>{{locationString}}</h1>
            </div>
        </div>
    </div>
</template>
<style scoped>
@import url('../styles/DeviceInfo.css');
</style>
<script>
import axios from 'axios';
import Spinner from '@/components/Spinner.vue';
export default {
    name: 'DeviceInfo',
    data() {
        return {
            timeString: '',
            locationData: {},
            isLoading: true
        }
    },
    methods: {
        updateTimeString() {
            this.timeString = new Date().toLocaleTimeString().slice(0, 5);
        }
    },
    computed: {
        locationString() {
            return (this.locationData.city ? this.locationData.city+',' : ' ') + this.locationData.country_name;
        }
    },
    mounted() {
        this.updateTimeString();
        setInterval(()=>{
            this.updateTimeString();
        }, 10000);
        axios.get("https://geolocation-db.com/json/")
            .then((resp) => {
                this.locationData = resp.data;
                setTimeout(() => {
                        this.isLoading = false;
                    }, 1000);
            })
    },
    components: {
        Spinner
    }
}
</script>