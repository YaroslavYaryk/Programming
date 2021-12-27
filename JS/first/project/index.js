
const PORT = process.env.PORT || 5000;
const Application = require('./framework/Application');
const userRouter = require('./database/user-router');
const jsonParser = require('./framework/parseJson');
const parseUrl = require('./framework/parseUrl');
const mongoose = require('mongoose');

const app = new Application()

app.use(jsonParser);
app.use(parseUrl('http://localhost:5000'));

app.addRouter(userRouter);


const start = async () => {
    try {
        await mongoose.connect('mongodb+srv://yaroslav:proshnik31@cluster0.or3e4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        app.listen(PORT, () => console.log(`Server started on PORT ${PORT}`))
    } catch (e) {
        console.log(e)
    }
}

start()