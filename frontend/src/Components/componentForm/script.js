export default {
  name: 'componentForm',
  props: ['fieldInfo'],
  data () {
    return {
    }
  },

  computed: {
    getFieldName () {
      return (this.fieldInfo.field_name)
    },
    getFieldType () {
      return (this.fieldInfo.field_type)
    },
    getFieldInfo () {
      return (this.fieldInfo)
    }
  }
}
