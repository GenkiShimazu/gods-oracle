from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name
from ask_sdk_model import ui
from util import assets


class AudienceSeatHandler(AbstractRequestHandler):
    """
    客席
    """

    def can_handle(self, handler_input):
        session = handler_input.attributes_manager.session_attributes
        scene = session.get('scene')
        if not scene:
            return False
        return scene == 'explore.colosseum' \
            and is_intent_name("AudienceSeatIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = """
        勇者「客席ですね！どんな手がかりがあるんだろう...？」
        読書している人「やぁ。どうかした？」
        勇者「実は訳あって、キャリネズミというモンスターをさがしているんだ。君はみていない？」
        読書している人「ごめん、読書に夢中で。あ！でもキャリネズミって、確かものすごく隠れるのが得意なモンスターだよね？」
        勇者「そうなんだよ！そのせいでさがし辛くて困っているんだ」
        読書している人「確か図書館でそんな感じの本を読んだ事がある気がするなぁ。うちの図書館はいろんな本があって、情報ならたいてい揃うよ」
        勇者「そっか！ありがとう！」
        読書している人「うん、がんばってねー！」
        <audio src="soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_intro_01"/>
        勇者「うーん、他に手がかりがありそうなのはどこだろう、、、？」
        """
        handler_input.response_builder.speak(
            speech_text).set_should_end_session(False)

        session = handler_input.attributes_manager.session_attributes
        session['scene'] = 'explore.colosseum'
        session['oracle_limit'] = session['oracle_limit'] - 1
        session['re_ask'] = '勇者「他に手がかりがありそうなのはどこだろう、、、？」'

        image_url = assets.get_image(
            'humans/hero/hero_stand_512')
        handler_input.response_builder.set_card(
            ui.StandardCard(
                title='勇者「他に手がかりがありそうなのはどこだろう、、、？」',
                text='・客席\r\n'
                     '・倉庫\r\n'
                     '・控室\r\n'
                     '・図書館へ行く\r\n'
                     '・闘技場へ行く\r\n'
                     '・屋上へ行く',
                image=ui.Image(
                    small_image_url=image_url,
                    large_image_url=image_url
                )
            )
        )

        return handler_input.response_builder.response
