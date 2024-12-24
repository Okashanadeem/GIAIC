import { type SchemaTypeDefinition } from 'sanity'
import { studentSchema } from '../student'
import { teacherSchema } from '../teacher'

export const schema: { types: SchemaTypeDefinition[] } = {
  types: [studentSchema,teacherSchema]
}
