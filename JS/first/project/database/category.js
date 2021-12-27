const mongo = require("mongoose")
// const {use} = require("express")
const Schema = mongo.Schema

const category = new Schema({
    name :{
        type:String,
        required:true
    },
    img :{
        type:String,
        default:""
    },
    user: {
        ref: "users",
        type: Schema.Types.ObjectId
    }
    

})

module.exports = mongo.model("categories", category)