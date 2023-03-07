<template>
  <div class="form">
    <form @submit.prevent="submitForm">
      <p class="font1">Title___of___Playlist:</p>
      <input type="text" class="userInput" v-model="form.playlistTitle">
      <p v-if="titleCheck" class="red-text">Please enter a valid title for playlist</p>
      <div class="spacer"></div>
      <p class="font1">Enter___Description:</p>
      <textarea name="description" cols="30" rows="5" v-model="form.playlistDesc"></textarea>
      <p v-if="descCheck" class="red-text">Please enter a valid title for description</p>
      <div class="listoptions">
        <div class="spacer"></div>
        <p class="font1">Choose___categories___of___anime:</p>
        <ul>
          <li v-for="(item,index) in listOptionstr" :key="index">
            <input type="checkbox" v-model="form.listOptions" :id="item.value" :value="item.value">
            <label for="{{ item.value }}" class="font4">{{ item.label }}</label>
          </li>
          <li>
          <input type="checkbox" id="all" v-model="listAll" @change="checkAll">
          <label for="all" class="font4"> All</label>
          </li>
        </ul>
      </div>
      <p v-if="listCheck" class="red-text">Please select at least one option</p>
      <div class="listoptions">
        <div class="spacer"></div>
        <p class="font1">Choose___types___of___songs:</p>
        <ul>
          <li v-for="item in songTypeStr">
            <input type="checkbox" v-model="form.songTypes" :id="item.value" :value="item.value">
            <label class="font4">{{ item.label }}</label>
          </li>
        </ul>
      </div>
      <p v-if="songCheck" class="red-text">Please select at least one option</p>
      <div class="spacer"></div>
      <button type="submit">Submit</button>
      <div class="spacer"></div>
      <img src="@/assets/images/Chopper.png" alt="centered image" style="max-width: 20%; float: right;">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'makePlaylist',
  props: {
    msg: String
  },
  data(){
    return {
      form : {
        playlistTitle: '',
        playlistDesc: '',
        listOptions : [],
        songTypes : []
      },
      titleCheck: false,
      descCheck: false,
      listCheck: false,
      songCheck: false,
      listAll: false,
      listOptionstr: [
      {label: ' Watching',value: 'watching'},
      {label: ' Completed',value: 'completed'},
      {label: ' On Hold', value: 'on_hold'},
      {label: ' Dropped', value: 'dropped'},
      {label: ' Plan To Watch', value: 'plan_to_watch'}
      ],
      songTypeStr: [
        {label: ' Openings', value: 'op'},
        {label: ' Endings', value: 'ed'}
      ]
    }
  },
  methods: {
    checkAll(){
      if(this.listAll){
        this.form.listOptions = ['watching','completed','on_hold','dropped','plan_to_watch']
      }
      else{
        this.form.listOptions = []
      }
    },
    checkForm(){
      if(this.form.playlistTitle == ''){
        this.titleCheck = true
      }
      else{
        this.titleCheck = false
      }
      if(this.form.playlistDesc == ''){
        this.descCheck = true
      }
      else{
        this.descCheck = false
      }
      if(this.form.listOptions.length == 0){
        this.listCheck = true
      }
      else{
        this.listCheck = false
      }
      if(this.form.songTypes.length == 0){
        this.songCheck = true
      }
      else{
        this.songCheck = false
      }
      if(this.songCheck || this.listCheck || this.descCheck || this.titleCheck){
        return false
      }
      else{
        return true
      }
      
    },
    submitForm(){
    
      if(!this.checkForm()){
        return
      }
      
      axios
      .post('http://127.0.0.1:5173/api/submission', this.form)
      .then(res =>{
        console.log(res.data)
      })
      .catch(error =>{
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>
.center {
  display: flex;
  justify-content: right;
  align-items: right;
  height: 20vh;
  margin-bottom: 100px;
  background-color: black;
}
.font1 {
  font-family: "Naruto", sans-serif;
  font-size: 30px;
  text-shadow: 1px 1px 10px rgba(0, 0, 0, 0.5);
  
  background-color: rgba(159, 0, 135, 0.452);
}

.font4 {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 20px;
  font-weight: bold;
  text-shadow: 1px 1px 5px rgba(0, 0, 0, 0.5);
}

.spacer {
  height: 50px; /* adjust as needed */
}

.red-text {
  color: red;
  font-weight: bold;
}
input[type="checkbox"] {
  height: 20px;
  width: 20px;
}
button[type="submit"] {
  font-family: "Naruto", sans-serif;
  font-size: 20px;
  padding: 10px 20px;
  background-color: rgb(255, 187, 0) !important;
}
</style>
