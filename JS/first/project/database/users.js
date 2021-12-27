const mongo = require("mongoose")
// const {use} = require("express")
const Schema = mongo.Schema

const users = new Schema({
    Email :{
        type:String,
        required:true,
    },
    Password :{
        type:String,
        required:true
    },
})

module.exports = mongo.model("users", users)