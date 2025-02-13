from astrbot import logger
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.provider import ProviderRequest
from astrbot.api.star import Context, Star, register
from astrbot.core.message.components import ComponentTypes


@register("astrbot-persistence", "moyuyanli", "一个对于消息进行持久化的插件", "1.0.0",
          "https://github.com/Moyuyanli/astrbot-plugin-persistence")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    # @filter.command("helloworld")
    # async def helloworld(self, event: AstrMessageEvent):
    #     '''这是一个 hello world 指令'''  # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
    #     user_name = event.get_sender_name()
    #     message_str = event.message_str  # 用户发的纯文本消息字符串
    #     message_chain = event.get_messages()  # 用户所发的消息的消息链 # from astrbot.api.message_components import *
    #     logger.info(message_chain)
    #     yield event.plain_result(f"Hello, {user_name}, 你发了 {message_str}!")  # 发送一条纯文本消息
    #
    # @event_message_type(EventMessageType.ALL)
    # async def on_private_message(self, event: AstrMessageEvent):
    #     '''测试消息'''
    #
    #     message_link = event.message_obj.message
    #     images = [component for component in message_link if isinstance(component, ComponentTypes.get("image"))]
    #
    #     if images:
    #         for img in images:
    #             logger.info(f"图片信息: {img}")  # 假设 Image 类有一个 'path' 属性
    #             yield event.image_result(img.file)
    #     else:
    #         yield event.plain_result(f"收到了一条消息,类型{event.message_obj.type.name}")

    @filter.on_llm_request()
    async def my_custom_hook_1(self, event: AstrMessageEvent, req: ProviderRequest):
        # 检查消息是否为纯文本消息
        if isinstance(event.message_obj.message, list) and all(
                isinstance(msg, ComponentTypes.get("text")) for msg in event.message_obj.message):
            # 进一步检查每个文本消息是否为空
            for msg in event.message_obj.message:
                if not msg.content or not msg.content.strip():
                    raise ValueError("消息内容不能为空")
        else:
            event.stop_event()
        logger.info(req)  # 打印请求的文本
