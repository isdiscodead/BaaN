document.write("<script src='https://code.jquery.com/jquery-3.3.1.min.js'></script>");

//// 모달 관련 오류 해결
//$(document).on({
//    'show.bs.modal': function() {
//      var zIndex = 1040 + (10 * $('.modal:visible').length);
//      $(this).css('z-index', zIndex);
//
//      setTimeout(function() {
//        $('.modal-backdrop').not('.modal-stack').css('z-index', zIndex - 1).addClass('modal-stack');
//      }, 0);
//    },
//
//    'hidden.bs.modal': function() {
//
//      if ($('.modal:visible').length > 0) {
//        // restore the modal-open class to the body element, so that scrolling works
//        // properly after de-stacking a modal.
//        setTimeout(function() {
//          $(document.body).addClass('modal-open');
//          $(".modal-backdrop").remove();
//          $('body').removeClass('modal-open');
//          $('body').css('padding-right', '');
//        }, 0);
//      }
//   }
//}, '.modal');

// 북마크 앱
function load_bookmark() {
    $.ajax({
        type: 'GET',
        url: '/bookmarks/list/',

        // 통신 성공
        success: function(result){
            $('#bookmark').html(result);
            // document.getElementById("bookmark").innerHTML(result);
        },

        // 통신 실패
        error: function(result) {
            alert("error!");
        }
    });
}

// 투두앱
function load_todo() {
    $.ajax({
        type: 'GET',
        url: '/todos/list/',

        // 통신 성공
        success: function(result){
            $('#todo').html(result);
            // document.getElementById("bookmark").innerHTML(result);
        },

        // 통신 실패
        error: function(result) {
            alert("error!");
        }
    });
}


