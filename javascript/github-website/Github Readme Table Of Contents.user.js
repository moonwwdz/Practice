// ==UserScript==
// @name         Github Readme Table Of Contents
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Show table of contents of github website content's left...
// @author       Moonwwdz
// @grant        none
// @match        *://github.com/*
// @require      https://cdn.bootcss.com/jquery/1.12.4/jquery.min.js
// ==/UserScript==

//仿自：http://www.jianshu.com/u/c887880e8f06

var $ = $ || window.$;
var url = "";
// 在侧边栏中添加目录项
function appendMenuItem(tagName,id,content){
    console.log(tagName+" "+tagName.substring(1));
    let paddingLeft = tagName.substring(1) * 30; //添加标题缩进
    $('#menu_nav_ol').append('<li class="' + id +'" style="padding-left: '+ paddingLeft +'px;"><b>' + content + '</b></li>');
}

function render(){
    let titles = $("#readme article").find('h1,h2,h3,h4,h5,h6');
    if(titles.length >0){
        console.log(titles);
        let contentHeight = window.innerHeight; //设置目录高度
        let asideContent = '<aside id="sideMenu" style="position: fixed;padding: 20px 15px 20px 15px;top: 0;right: 0;margin-bottom:20px;background-color: #eee;background-color: #eee;z-index: 810;overflow: scroll;max-height:'+contentHeight+'px;min-height:'+contentHeight+'px;min-width:350px;max-width:350px;"><h2>Table Of Contents<h2></aside>';

        $("#js-repo-pjax-container").append(asideContent)
        $('#sideMenu').append('<ol id="menu_nav_ol" style="list-style:none;margin:0px;padding:0px;">');// 不显示 li 项前面默认的点标志, 也不使用默认缩进

        titles.each(function(){
            let tagName = $(this)[0].tagName.toLocaleLowerCase();
            let content = $(this).text();
            let newTagId = $(this).find("a").attr('id')
            appendMenuItem(tagName,newTagId,content);
        });
        $('#sideMenu').append('</ol>');
        // 绑定目录li点击事件,点击时跳转到对应的位置
        $('#menu_nav_ol li').on('click',function(){
            let targetId = $(this).attr('class');
            $("#"+targetId)[0].scrollIntoView(true);
        });
        url = location.href;
    }
}


(function() {
    'use strict';   
    render();
    setInterval(function(){
        console.log(url,location.href);
        if( url != location.href){
            render()
        }
    },5000)
})();