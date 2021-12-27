const express = require('express')
const mongo = require("mongoose")
const Post = require("./post")


const DB_URL = 'mongodb+srv://yaroslav:proshnik31@cluster0.or3e4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
const PORT = 5000

const app = express()
app.use(express.json())

app.get("/", async (req, res) => {
    const post = await Post.find()
    res.status(200).json(post)
})

app.post("/", async (req, res) => {
    try{
        const {author, title, content, picture} = req.body
        const post = await Post.create({author, title, content, picture})
        res.status(200).json(post)
    }catch(err){
        res.status(500).json(err)
    }
    
})

async function startapp(){
    try{
        await mongo.connect(DB_URL)
        app.listen(PORT, () => console.log("SERVER IS RUNNING"))
    } catch (e){
        console.log(e)
    }
}

startapp()




