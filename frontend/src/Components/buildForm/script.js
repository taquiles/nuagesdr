import Vue from 'vue'
import componentForm from '../componentForm/index'

Vue.component('component-enum', {
  props: ['fieldInfo'],
  template: '\
    <b-field class="container" :label="fieldInfo.field_name">\
      <b-select placeholder="Select">\
        <option\
          v-for="fieldEnum in fieldInfo.enum_value"\
          :value="fieldEnum.enum_value"\
          :key="fieldEnum.enum_value">\
          {{ fieldEnum.enum_value }}\
        </option>\
      </b-select>\
    </b-field>'
})

Vue.component('component-date', {
  props: ['fieldInfo'],
  template: '\
    <b-field class="container" :label="fieldInfo.field_name">\
        	<b-datepicker\
        	  placeholder="Click to select..."\
        	>\
    		</b-datepicker>\
    </b-field>'
})

Vue.component('component-TextNumber', {
  props: ['fieldInfo'],
  template: '\
      <section>\
      <b-field :label="fieldInfo.field_name">\
        <b-input \
          placeholder=""\
          :type="fieldInfo.field_type"\
        >\
        </b-input>\
      </b-field>\
    </section>'    
})

export default {
  name: 'buildForm',
  components: {
    componentForm
  },
  props: ['riskType'],
  data () {
    return {
    }
  },

  computed: {
    getRiskTypeName () {
      return (this.riskType.riskType.risk_type_name)
    },
    getRiskTypeFieldNames () {
      return (this.riskType.riskType.field_info)
    }
  }
}
