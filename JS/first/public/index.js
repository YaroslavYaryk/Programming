// const chalk = require("chalk")
// const text = require("./data")
// const os = require("os")


// console.log(chalk.blue("Hello Python"))
// console.log(os.cpus())

const http = require("http")
const fs = require("fs")
const path = require("path")



const server = http.createServer((req, res) => {

    if (req.url === "/"){
        fs.readFile(path.join(__dirname, "public", "index.html"), (err, data) =>{
            if (err){
                throw err
            }
            res.writeHead(200, Headers={
                "Content-Type" : "text/html"
            })
            res.end(data)
            
        })
    }
    if (req.url === "/users"){
    
        res.writeHead(200, Headers={
            "Content-Type" : "application/json"
        })
        data = [{"name" : "Yaroslav", "surname" : "Dyhanov"},
                {"name" : "Roma", "surname" : "Romanov"}]
        res.end(JSON.stringify(data))
    }

    console.log(req.url)    
})

server.listen(3000, () =>{
    console.log("server has been started")
})