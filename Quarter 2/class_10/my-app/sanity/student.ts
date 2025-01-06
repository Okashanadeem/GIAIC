import { defineType } from 'sanity';

export const studentSchema = defineType({
  name: 'student',
  title: 'Student Profile',
  type: 'document',
  fields: [
    {
      name: 'name',
      title: 'Student Name',
      type: 'string',
    },
    {
      name: 'age',
      title: 'Student Age',
      type: 'number',
      hidden: ({document}:any) => document.name === "Okasha"
    },
    {
      name: 'gender',
      title: 'Gender',
      type:'string',
      options:{
        list:[
          {title:"Male", value:"male"},
          {title:"Female", value:"female"},
          {title:"Other", value:"other"}
        ],
        layout : 'dropdown'
      }
    },
    {
      title: 'Address',
      name: 'address',
      type: 'object',
      fields: [
        {name: 'street', type: 'string', title: 'Street name'},
        {name: 'streetNo', type: 'string', title: 'Street number'},
        {name: 'city', type: 'string', title: 'City'}
      ]
    },
    {
      title: 'Is student still studying?',
      name: 'studying',
      type: 'boolean'
    },
    {
      title: 'Image',
      name: 'image',
      type: 'image',
      options: {
        hotspot: true // <-- Defaults to false
      },
    },
    {
      title: 'About', 
      name: 'about',
      type: 'array', 
      of: [{type: 'block'}]
    },
    {
      type: 'object',
      name: 'person',
      fieldsets: [
        {name: 'social', title: 'Social media handles'}
      ],
      fields: [
        {
          title: 'Name',
          name: 'name',
          type: 'string'}]
    }
  ],
}
);
