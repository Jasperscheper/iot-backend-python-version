<script setup>
    import Dashboard from "./components/Dashboard.vue"
</script>


<template>
    <Suspense>
        <div class="container mx-auto">
            <Dashboard></Dashboard>
        </div>
       
    </Suspense>
</template>


<style>
    .container {
        display: flex;
        width: 100vw;
        flex-direction: column;
    }

    .header {
        width: 100%;
        text-align: center;
    }

    .main{
        width: 100%;
    }
</style>