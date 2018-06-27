// ==UserScript==
// @name         ����Ŀ¼
// @description:zh-cn �Զ����ɼ���Ŀ¼
// @namespace    http://www.jianshu.com/u/c887880e8f06
// @version      1.0
// @description  create content
// @author       Wonder233
// @match        *://www.jianshu.com/p/*
// @require           https://cdn.bootcss.com/jquery/1.12.4/jquery.min.js
// @grant        none
// ==/UserScript==
var menuIndex = 0; //��ʼ����������

console.log("let let let:::::::");
var $ = $ || window.$;
// �ڲ���������Ŀ¼��
function appendMenuItem(tagName,id,content){
    console.log(tagName+" "+tagName.substring(1));
    let paddingLeft = tagName.substring(1) * 30; //��ӱ�������
    $('#menu_nav_ol').append('<li class="' + id +'" style="padding-left: '+ paddingLeft +'px;"><b>' + content + '</b></li>');
}

(function() {
    'use strict';
    // ʹ����������������Ļ
    let wider = $('.note').width() - 400;
    console.log(wider);
    let oriWidth = $('.post').width();
    console.log(wider);
    console.log(oriWidth);
    if (wider < oriWidth){
       wider = oriWidth;
    }
    // ������
    $('.post').width(wider);

    // �������Ԫ��
    let titles = $('body').find('h1,h2,h3,h4,h5,h6');
    if(titles.length === 0){
        return;
    }
    // ��������������
    $('.post').css('padding-left','200px');
    // �� body ��ǩ�ڲ���� aside �����,������ʾ�ĵ�Ŀ¼
    let contentHeight = window.innerHeight; //����Ŀ¼�߶�
    let asideContent = '<aside id="sideMenu" style="position: fixed;padding: 80px 15px 20px 15px;top: 0;left: 0;margin-bottom:20px;background-color: #eee;background-color: #eee;z-index: 810;overflow: scroll;max-height:'+contentHeight+'px;min-height:'+contentHeight+'px;min-width:350px;max-width:350px;"><h2>Ŀ¼<h2></aside>';
    $('.show-content').prepend(asideContent);
    $('#sideMenu').append('<ol id="menu_nav_ol" style="list-style:none;margin:0px;padding:0px;">');// ����ʾ li ��ǰ��Ĭ�ϵĵ��־, Ҳ��ʹ��Ĭ������

    // ���������е����б�����, �������idֵ, �����Ӽ�¼��Ŀ¼�б���
    titles.each(function(){
          let tagName = $(this)[0].tagName.toLocaleLowerCase();
          let content = $(this).text();
          // �������id������,��ʹ����id
          let newTagId =$(this).attr('id');
          if(!$(this).attr('id')){
              newTagId = 'id_'+menuIndex;
              $(this).attr('id',newTagId);
              menuIndex++;
          }
          if(newTagId !=='id_0'){ //���Ա���
              appendMenuItem(tagName,newTagId,content);
          }
    });

    $('#sideMenu').append('</ol>');
    // ��Ŀ¼li����¼�,���ʱ��ת����Ӧ��λ��
    $('#menu_nav_ol li').on('click',function(){
        let targetId = $(this).attr('class');
        $("#"+targetId)[0].scrollIntoView(true);
    });
})();
