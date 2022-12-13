<script setup>

    import { reactive, computed, watch } from 'vue'
    import axios from "axios";

    import { Line } from 'vue-chartjs'
    import 'chart.js/auto'

    const alarms = await axios.get("http://localhost:5000/alarms").then(res => res.data).then(res =>{
                return res;
            })

    const state = reactive({ alarms, 'selectedDevice': null, weatherData: null, amountOfHours:  24, updatedLocation: ''})

    const getWeatherData = async () => {
        if(state.selectedDevice !== null){
            let weatherData =  await axios.get(`http://localhost:5000/alarms/${state.selectedDevice.macAddress}/weather`).then(res => res.data).then(res => {return res});
            state.weatherData = weatherData
        }
    }

    const weatherData = computed(() => {
        if (state.weatherData == null){
            return [];
        }
        return {
            labels: state.weatherData?.hourly !== null ? state.weatherData?.hourly?.time.slice(0, state.amountOfHours) : [],
            datasets: [{
                label: 'Temperatuur',
                data: state.weatherData?.hourly !== null ? state.weatherData?.hourly?.temperature_2m.slice(0, state.amountOfHours) : [],
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }]
        }
    })

    watch(() => state.selectedDevice, () => {
        getWeatherData();
        state.updatedLocation = state.selectedDevice.location;
    })

    const updateLocation = () => {
        axios.get(`http://localhost:5000/alarms/${state.selectedDevice.macAddress}/setLocation?location=${state.updatedLocation}`);
        getWeatherData();
    }
</script>


<template>
    <div class="container">
        <div class="main">
            <div class="flex justify-center mt-16">
                <div class="mb-3 xl:w-96">
                    <p class="text-2xl pb-2">Selecteer een wekker</p>
                    <select class="form-select appearance-none
                    block
                    w-full
                    px-3
                    py-1.5
                    text-base
                    font-normal
                    text-gray-700
                    bg-white bg-clip-padding bg-no-repeat
                    border border-solid border-gray-300
                    rounded
                    transition
                    ease-in-out
                    m-0
                    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" aria-label="Default select example"
                    v-model="state.selectedDevice"
                    >
                        <option selected disabled>Select a device</option>
                        <option v-for="(alarm, key) in state.alarms" :key="key" :value="alarm">{{alarm.macAddress}}</option>
                    </select>
                </div>
            </div>  
            <div class="flex justify-center mt-16">
                <div v-if="state.selectedDevice !== null">
                    <p>Geselecteerde wekker: {{ state.selectedDevice.macAddress}}</p>
                    <p>Weer locatie: {{ state.selectedDevice.location}}</p>

                    <input 
                    type="text"
                    class="form-select appearance-none
                    block
                    w-full
                    px-3
                    py-1.5
                    text-base
                    font-normal
                    text-gray-700
                    bg-white bg-clip-padding bg-no-repeat
                    border border-solid border-gray-300
                    rounded
                    transition
                    ease-in-out
                    m-0
                    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" aria-label="Default select example"
                    v-model="state.updatedLocation"
                    >
                    <button class="bg-blue-400 text-white px-3 py-1.5 my-4" @click="updateLocation">Save location</button>
                    <p>Forecast amount of hours </p>
                    <input type="number" class="form-select appearance-none
                    block
                    w-full
                    px-3
                    py-1.5
                    text-base
                    font-normal
                    text-gray-700
                    bg-white bg-clip-padding bg-no-repeat
                    border border-solid border-gray-300
                    rounded
                    transition
                    ease-in-out
                    m-0
                    focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" v-model="state.amountOfHours" min="12" :max="state?.weatherData?.hourly?.temperature_2m?.length">
                    <Line
                        v-if="state.chartData !== null && state.selectedDevice.location !== null"
                        :chart-options="[]"
                        :chart-data="weatherData"
                        :chart-id="'1'"
                        :width="300"
                        :height="300"
                    />
                </div>
            <div v-else>
                <p>Je hebt nog geen wekker geselecteerd</p>
            </div>
            </div>
        </div>
       
    </div>
</template>