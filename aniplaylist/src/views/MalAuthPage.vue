<template>
    <MALAuth />
</template>
  
<script>
import MALAuth from '../components/MALAuth.vue';

export default {
    name: "Search",
    data(){
    return {
        MALSuccess: false,
    }
    },
    components: { MALAuth },
    methods: {
    spot(){
        this.spotSuccess = true;
        this.checkAuth()
    },
    checkAuth(){
        if(this.MALSuccess == true){
        this.$router.push('/options');
        }
    }
    
    },
    beforeUpdate(){
    this.checkAuth();
    }
}
</script>