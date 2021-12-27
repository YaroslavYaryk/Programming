const Users = require("./users")

const getUsers = async (req, res) => {
    res.send(await Users.find())
}

module.exports = {
    getUsers,
}