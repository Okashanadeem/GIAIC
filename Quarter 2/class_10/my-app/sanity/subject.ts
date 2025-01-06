import { defineField, defineType } from "sanity"
export const subjectSchema = defineType({
    name: "subject",
    type: "document",
    title: "Subjects",
    fields:[defineField({
        name:"subject",
        type: "string",
        title: "Choose subject"
    })]
})