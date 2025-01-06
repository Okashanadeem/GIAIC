import { type SchemaTypeDefinition } from 'sanity'
import { studentSchema } from '../student'
import { teacherSchema } from '../teacher'
import { subjectSchema } from '../subject'
import { testSchema } from '../test'

export const schema: { types: SchemaTypeDefinition[] } = {
  types: [studentSchema,teacherSchema,subjectSchema,testSchema]
}
