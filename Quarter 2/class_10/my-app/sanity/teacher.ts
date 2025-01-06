import { defineType } from 'sanity';

export const teacherSchema = defineType({
  name: 'teacher',
  title: 'Teacher Profile',
  type: 'document',
  fields: [
    {
      name: 'name',
      title: 'Teacher Name',
      type: 'string',
    },
    {
      name: 'age',
      title: 'Student Age',
      type: 'number',
      readOnly: ({document}:any) => document.name === "Ali"
    },
    {
      name: 'subject',
      title: 'Subject Taught',
      type: 'string',
      hidden: ({document}:any) => document.age <= 20
    },
    {
      title: 'Address',
      name: 'address',
      type: 'object',
      fields: [
        { name: 'street', type: 'string', title: 'Street name' },
        { name: 'streetNo', type: 'string', title: 'Street number' },
        { name: 'city', type: 'string', title: 'City' }
      ]
    },
    {
      title: 'About',
      name: 'about',
      type: 'array',
      of: [{ type: 'block' }]
    },
    {
      name:"subjectTeach",
      title: "Subject Teach",
      type: "reference",
      to:[{type:"subject"}]
    },
    {
      name: 'others',
      title: 'Others',
      type: 'array',
      of: [
        {
          type: 'reference',
          to: [
            {type: 'subject'},
          ]
        }
      ]
    } 
  ],
});