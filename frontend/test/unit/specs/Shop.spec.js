import Shop from '@/components/Shop'
import { shallowMount } from '@vue/test-utils'

describe('Shop.vue', () => {
  it('should render correct contents', () => {
    const msg = 'This is an ACME page'
    const wrapper = shallowMount(Shop, {
      propsData: { msg }
    })
    expect(wrapper.text()).toMatch(msg)
    // const Constructor = Vue.extend(Shop)
    // const vm = new Constructor().$mount()
    // expect(vm.$el.querySelector('.hello h1').textContent)
    //   .toEqual('Welcome to Your Vue.js App')
  })
})
