import { Client } from 'pg';
import dotenv from 'dotenv';
import { Student } from './types';

dotenv.config({ path: `${process.cwd()}/../.env` });
const connectionString = `postgres://${process.env.PGUSER}:${process.env.PGPASSWORD}@${process.env.PGHOST}:${process.env.PGPORT}/${process.env.PGDATABASE}`

export async function student(args: { id: string }): Promise<Student | null> {
  const client = new Client(connectionString);
  await client.connect();

  const res = await client.query('select * from students where id = $1::uuid', [args.id]);
  await client.end();

  return res.rows.length > 0 ? res.rows[0] : null;
}

export async function students(): Promise<Student[]> {
  const client = new Client(connectionString);
  await client.connect();

  const res = await client.query('select * from students');
  await client.end();

  return res.rows as Student[];
}
