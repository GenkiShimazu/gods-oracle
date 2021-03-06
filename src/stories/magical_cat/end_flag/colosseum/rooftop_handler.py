from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_intent_name
from ask_sdk_model import ui
from util import assets


class RooftopIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input):
        session = handler_input.attributes_manager.session_attributes
        scene = session.get('scene')
        if not scene:
            return False
        return scene == 'end_flag.colosseum' and \
            is_intent_name("RooftopIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = """
        勇者「屋上ですね！かしこまりました！」
        <audio src="soundbank://soundlibrary/human/amzn_sfx_person_running_03"/>
        勇者「音を聞くんじゃない！何も聞こえないところに耳をすますんだ！」
        盲目の生徒「そうか、、、わかった！やってみる！」
        <audio src="soundbank://soundlibrary/backgrounds_ambience/public_space/public_space_01"/>
        <audio src="soundbank://soundlibrary/kids/kids_05"/>
        <break time="3s"/>
        盲目の生徒「わかったぞ！闘技場の倉庫の裏だ！」
        勇者「す、すごい！ありがとう！行こう！」
        <audio src="soundbank://soundlibrary/human/amzn_sfx_person_running_03"/>
        勇者「先生、闘技場の倉庫の裏です！」
        先生「え、わ、わかったわ！」
        <audio src="soundbank://soundlibrary/human/amzn_sfx_person_running_03"/>
        <break time="2s"/>
        勇者「すごいよ！本当に見つけてしまうなんて！」
        先生「やっぱりあなたは天才よ！」
        盲目の生徒「たいしたことはしてないよ。」
        勇者「いいや、紛れもない、本当の天才だ！」
        先生「あなたにここまでの才能があったなんて！」
        盲目の生徒「あ、ありがとうございます！」
        いじめっこB「わ、わるかったな」
        いじめっこA「たすかったぜ。恩に着る。」
        盲目の生徒「うん。」
        <break time="2s"/>
        こうして、ソルジャースクールのみんなは救われ、平穏をとりもどした。
        勇者はソルジャースクールを後にし、旅立った。
        この盲目の生徒が、後に「盲目の狩人」と呼ばれるのは、また別のお話。
        <break time="3s"/>
        おしまい。
        
        <break time="3s"/>
        オルぺ「課題クリアおめでとう！君、才能ありまちゅね。
        次は、どの課題に挑戦しまちゅか？」
        """
        handler_input.response_builder.speak(
            speech_text).set_should_end_session(False)

        session = handler_input.attributes_manager.session_attributes
        session['scene'] = 'gods_world'
        session['re_ask'] = 'オルぺ「どの課題に挑戦しまちゅか？」'

        image_url = assets.get_image(
            'humans/blind_hunter/blind_hunter_found_512')
        handler_input.response_builder.set_card(
            ui.StandardCard(
                title='盲目の生徒',
                text='「わかったぞ！闘技場の倉庫の裏だ！」',
                image=ui.Image(
                    small_image_url=image_url,
                    large_image_url=image_url
                )
            )
        )

        return handler_input.response_builder.response
