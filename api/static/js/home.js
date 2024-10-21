$(function() {
  /* NOTE: hard-refresh the browser once you've updated this */
  $(".typed").typed({
    strings: [
      "Hello I'm Yassine EL OUAFI<br/>" +
      "><span class='caret'>$</span> job: Data & Software Engineer freelance<br/> ^100" +
      "><span class='caret'>$</span> skills: Python, Spark , Airflow , Docker, Kafka, RabbitMQ<br/> ^100" +
      "><span class='caret'>$</span> hobbies: Chess , Football, Coding <br/> ^300" +
      "><span class='caret'>$</span> alias: Yassel<br/> ^300" +
      "><span class='caret'>$</span> universe: found traces in every universe<br/> ^300"
    ],
    showCursor: true,
    cursorChar: '_',
    autoInsertCss: true,
    typeSpeed: 0.001,
    startDelay: 50,
    loop: false,
    showCursor: false,
    onStart: $('.message form').hide(),
    onStop: $('.message form').show(),
    onTypingResumed: $('.message form').hide(),
    onTypingPaused: $('.message form').show(),
    onComplete: $('.message form').show(),
    onStringTyped: function(pos, self) {$('.message form').show();},
  });
  $('.message form').hide()
});