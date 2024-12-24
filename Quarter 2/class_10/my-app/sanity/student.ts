import { list } from 'postcss';
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
      title: 'Image',
      name: 'image',
      type: 'image',
      options: {
        hotspot: true // <-- Defaults to false
      },
    }
  ],
}
);
