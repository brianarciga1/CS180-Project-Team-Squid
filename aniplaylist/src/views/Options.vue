<template>
  <div class="form">
    <form @submit.prevent="submitForm">
      <p class="prompt">Title of Playlist:</p>
      <input type="text" class="userInput" v-model="form.playlistTitle">
      <p v-if="titleCheck">Please enter a valid title for playlist</p>
      <p class="prompt">Enter Description:</p>
      <textarea name="description" cols="30" rows="5" v-model="form.playlistDesc"></textarea>
      <p v-if="descCheck">Please enter a valid title for description</p>
      <div class="listoptions">
        <p class="prompt">Choose catagories of anime:</p>
        <ul>
          <li v-for="(item,index) in listOptionstr" :key="index">
            <input type="checkbox" v-model="form.listOptions" :id="item.value" :value="item.value">
            <label for="{{ item.value }}">{{ item.label }}</label>
          </li>
          <li>
          <input type="checkbox" id="all" v-model="listAll" @change="checkAll">
          <label for="all">All</label>
          </li>
        </ul>
      </div>
      <p v-if="listCheck">Please select at least one option</p>
      <div class="listoptions">
        <p class="prompt">Choose types of songs:</p>
        <ul>
          <li v-for="item in songTypeStr">
            <input type="checkbox" v-model="form.songTypes" :id="item.value" :value="item.value">
            <label>{{ item.label }}</label>
          </li>
        </ul>
      </div>
      <p v-if="songCheck">Please select at least one option</p>
      <button type="submit">Submit</button>
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
      {label: 'Watching',value: 'watching'},
      {label: 'Completed',value: 'completed'},
      {label: 'On Hold', value: 'on_hold'},
      {label: 'Dropped', value: 'dropped'},
      {label: 'Plan To Watch', value: 'plan_to_watch'}
      ],
      songTypeStr: [
        {label: 'Openings', value: 'op'},
        {label: 'Endings', value: 'ed'}
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

</style>
