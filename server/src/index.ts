import express, { Express, Request, Response } from "express";
import dotenv from "dotenv";

const app: Express = express();
dotenv.config()

app.get('/', (req: Request, res: Response) => {
	res.status(200).json("working");
});

app.listen(process.env.EXPRESS_PORT, () => console.log(`(${process.env.EXPRESS_PORT}) SERVER RUNNING`));
