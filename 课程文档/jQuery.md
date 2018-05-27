查找元素

- 选择器
  - */ element / #id / .class / selector1, selector2(并列选择器)
  - ancestor descendant- $('#headr a')/ parent>child (父子选择器)/ previous+next(相邻兄弟选择器) / previous~siblings (平级兄弟选择器)
- 筛选器
  - 基本筛选器：:not(selector) 

    / :first / :last / :even--偶数 / :odd--奇数 / :eq(index) / :gt(index)--匹配所有比给定索引大的元素 / :lt(index)--匹配所有比给定索引小的元素 / :animated--匹配所有正在执行动画效果的元素 / :focus--匹配当前获得焦点的元素

  - 内容筛选器：:contains('…') --匹配所有text中的内容/ :empty / :parent / :has(selector)

  - 可见性筛选器：:hidden / :visible

  - 子节点筛选器：:nth-child(expr) / :first-child / :last-child / :only-child

  - 属性筛选器：attr[attribute]-div[id]/attr [attribute='value'] / attr[attribute!='value'] /attr [attribute^='value'] / attr[attribute$='value'] /attr [attribute|='value']  /attr[attribute~='value']
- 表单：:input / :text / :password / :radio / :checkbox / :submit / :image / :reset / :button / :file / :selected / :enabled / :disabled / :checked

执行操作

- 内容操作
  - 获取/修改内容：html() / text() / replaceWith() / remove()
  - 获取/设置/添加元素：before() / after() / prepend() / append() / remove() / clone() / unwrap() / detach() / empty() / add()
  - 获取/修改属性： css()/attr() / removeAttr() / addClass() / removeClass() 
  - 获取/设置表单值：val()
- 查找操作
  - 查找方法：find() /  parent() / children() / siblings() / next() / nextAll() / prev() / prevAll()
  - 筛选器：filter() / not() / has() / is() / contains()
  - 索引编号：eq()
- 尺寸和位置
  - 尺寸相关：height() / width() / innerHeight() / innerWidth() / outerWidth() / outerHeight()
  - 位置相关：offset() --获取匹配元素在当前视口的相对偏移(top,left)/ position() / scrollLeft() / scrollTop()
- 特效和动画
  - 基本动画：show() / hide() / toggle()
  - 消失出现：fadeIn() / fadeOut() / fadeTo() / fadeToggle()
  - 滑动效果：slideDown() / slideUp() / slideToggle()
  - 自定义：delay() / stop() / animate()
- 事件
  - 文档加载：ready() / load()
  - 用户交互：on() / off()

 jQuery 的$() 函数 

				// $(function(){}) - 作用:$函数中传入的参数是一个函数,该函数是页面加载完成之后执行的回调函数.
				// $(selector) - 作用:$函数中传入的参数是一个选择器,通过选择器获得对应的元素并将其处理成jQuery对象
				// $(elem) - 作用:$函数中传入的参数是原生的JS对象,将原生的JS对象转换成jQuery 对象.$(this)
				// $(tag) - 作用:$函数中的参数传入的是一个标签,创建和标签对应的元素(得到的是jQuery对象) $('<div>')
				
				// 通过jQuery 的对象可以用更少的代码做更多的事情,并且不用去考虑浏览器兼容性问题