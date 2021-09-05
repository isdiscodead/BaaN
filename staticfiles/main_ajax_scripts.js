document.write("<script src='https://code.jquery.com/jquery-3.3.1.min.js'></script>");

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

// 메모앱
function load_memo() {
    $.ajax({
        type: 'GET',
        url: '/memos/list/',

        // 통신 성공
        success: function(result){
            $('#memo').html(result);
            // document.getElementById("bookmark").innerHTML(result);
        },

        // 통신 실패
        error: function(result) {
            alert("error!");
        }
    });
}


