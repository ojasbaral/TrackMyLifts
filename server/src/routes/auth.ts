import { Router } from "express";
export const authRouter = Router();

authRouter.get('/', async (req, res, next) => {
	res.status(200).json("login");
});

