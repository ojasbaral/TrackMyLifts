import express, { Express, Request, Response } from "express";
import dotenv from "dotenv";
import bodyParser from "body-parser";
// import cookieParser from "cookie-parser";
import { authRouter } from './routes/auth'
const app: Express = express();
dotenv.config();

app.use(bodyParser.json());
// app.use(cookieParser());
app.use((req, res, next) => {
	console.log(req.method)
	console.log(req.url)
	console.log(req.body)
	console.log(req.params)
	next()
})
app.use('/auth', authRouter);

app.listen(process.env.EXPRESS_PORT, () => console.log(`(${process.env.EXPRESS_PORT}) SERVER RUNNING`));
