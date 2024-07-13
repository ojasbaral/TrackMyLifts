import pgPromise from "pg-promise";
import dotenv from "dotenv";
dotenv.config();

const config = {
	host: "db",
	port: 5432,
	database: process.env.POSTGRES_DB,
	user: process.env.POSTGRES_USER,
	password: process.env.POSTGRES_PASSWORD
};
const pgp = pgPromise();
export const db = pgp(config);
db.connect().then(() => {
	console.log("DB CONNECTED")
});
