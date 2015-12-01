(function($){
    var bigAutocomplete = new function(){
        this.currentInputText = null;//Ä¿Ç°»ñµÃ¹â±êµÄÊäÈë¿ò£¨½â¾öÒ»¸öÒ³Ãæ¶à¸öÊäÈë¿ò°ó¶¨×Ô¶¯²¹È«¹¦ÄÜ£©
        this.functionalKeyArray = [9,20,13,16,17,18,91,92,93,45,36,33,34,35,37,39,112,113,114,115,116,117,118,119,120,121,122,123,144,19,145,40,38,27];//¼üÅÌÉÏ¹¦ÄÜ¼ü¼üÖµÊý×é
        this.holdText = null;//ÊäÈë¿òÖÐÔ­Ê¼ÊäÈëµÄÄÚÈÝ
        
        //³õÊ¼»¯²åÈë×Ô¶¯²¹È«div£¬²¢ÔÚdocument×¢²ámousedown£¬µã»÷·ÇdivÇøÓòÒþ²Ødiv
        this.init = function(){
            $("body").append("<div id='bigAutocompleteContent' class='bigautocomplete-layout'></div>");
            $(document).bind('mousedown',function(event){
                var $target = $(event.target);
                if((!($target.parents().andSelf().is('#bigAutocompleteContent'))) && (!$target.is(bigAutocomplete.currentInputText))){
                    bigAutocomplete.hideAutocomplete();
                    }
                })
            
            //Êó±êÐüÍ£Ê±Ñ¡ÖÐµ±Ç°ÐÐ
            $("#bigAutocompleteContent").delegate("tr", "mouseover", function() {
                $("#bigAutocompleteContent tr").removeClass("ct");
                $(this).addClass("ct");
                }).delegate("tr", "mouseout", function() {
                    $("#bigAutocompleteContent tr").removeClass("ct");
                });
            
            
            //µ¥»÷Ñ¡ÖÐÐÐºó£¬Ñ¡ÖÐÐÐÄÚÈÝÉèÖÃµ½ÊäÈë¿òÖÐ£¬²¢Ö´ÐÐcallbackº¯Êý
            $("#bigAutocompleteContent").delegate("tr", "click", function() {
                bigAutocomplete.currentInputText.val( $(this).find("div:last").html());
                var callback_ = bigAutocomplete.currentInputText.data("config").callback;
                if($("#bigAutocompleteContent").css("display") != "none" && callback_ && $.isFunction(callback_)){
                    callback_($(this).data("jsonData"));
                    
                }
                bigAutocomplete.hideAutocomplete();
            })
            
            }
        
        this.autocomplete = function(param){
            
            if($("body").length > 0 && $("#bigAutocompleteContent").length <= 0){
                bigAutocomplete.init();//³õÊ¼»¯ÐÅÏ¢
            }
            
            var $this = $(this);//Îª°ó¶¨×Ô¶¯²¹È«¹¦ÄÜµÄÊäÈë¿òjquery¶ÔÏó
            
            var $bigAutocompleteContent = $("#bigAutocompleteContent");
            
            this.config = {
                               //width:ÏÂÀ­¿òµÄ¿í¶È£¬Ä¬ÈÏÊ¹ÓÃÊäÈë¿ò¿í¶È
                               width:$this.outerWidth() - 2,
                               //url£º¸ñÊ½url:""ÓÃÀ´ajaxºóÌ¨»ñÈ¡Êý¾Ý£¬·µ»ØµÄÊý¾Ý¸ñÊ½Îªdata²ÎÊýÒ»Ñù
                               url:null,
                               /*data£º¸ñÊ½{data:[{title:null,result:{}},{title:null,result:{}}]}
                                                urlºÍdata²ÎÊýÖ»ÓÐÒ»¸öÉúÐ§£¬dataÓÅÏÈ*/
                               data:null,
                               //callback£ºÑ¡ÖÐÐÐºó°´»Ø³µ»òµ¥»÷Ê±»Øµ÷µÄº¯Êý
                               callback:null};
            $.extend(this.config,param);
            
            $this.data("config",this.config);
            
            //ÊäÈë¿òkeydownÊÂ¼þ
            $this.keydown(function(event) {
                switch (event.keyCode) {
                    case 40://ÏòÏÂ¼ü
                    
                    if($bigAutocompleteContent.css("display") == "none")return;
                    
                    var $nextSiblingTr = $bigAutocompleteContent.find(".ct");
                    if($nextSiblingTr.length <= 0){//Ã»ÓÐÑ¡ÖÐÐÐÊ±£¬Ñ¡ÖÐµÚÒ»ÐÐ
                        $nextSiblingTr = $bigAutocompleteContent.find("tr:first");
                        }else{
                            $nextSiblingTr = $nextSiblingTr.next();
                            }
                    $bigAutocompleteContent.find("tr").removeClass("ct");
                    
                    if($nextSiblingTr.length > 0){//ÓÐÏÂÒ»ÐÐÊ±£¨²»ÊÇ×îºóÒ»ÐÐ£©
                        $nextSiblingTr.addClass("ct");//Ñ¡ÖÐµÄÐÐ¼Ó±³¾°
                        $this.val($nextSiblingTr.find("div:last").html());//Ñ¡ÖÐÐÐÄÚÈÝÉèÖÃµ½ÊäÈë¿òÖÐ
                        
                        //div¹ö¶¯µ½Ñ¡ÖÐµÄÐÐ,jquery-1.6.1 $nextSiblingTr.offset().top ÓÐbug£¬ÊýÖµÓÐÎÊÌâ
                        $bigAutocompleteContent.scrollTop($nextSiblingTr[0].offsetTop - $bigAutocompleteContent.height() + $nextSiblingTr.height() );
                        
                        }else{
                            $this.val(bigAutocomplete.holdText);//ÊäÈë¿òÏÔÊ¾ÓÃ»§Ô­Ê¼ÊäÈëµÄÖµ
                            }
                    
                    
                    break;
                    case 38://ÏòÉÏ¼ü
                    if($bigAutocompleteContent.css("display") == "none")return;
                    
                    var $previousSiblingTr = $bigAutocompleteContent.find(".ct");
                    if($previousSiblingTr.length <= 0){//Ã»ÓÐÑ¡ÖÐÐÐÊ±£¬Ñ¡ÖÐ×îºóÒ»ÐÐÐÐ
                        $previousSiblingTr = $bigAutocompleteContent.find("tr:last");
                        }else{
                            $previousSiblingTr = $previousSiblingTr.prev();
                            }
                    $bigAutocompleteContent.find("tr").removeClass("ct");
                    
                    if($previousSiblingTr.length > 0){//ÓÐÉÏÒ»ÐÐÊ±£¨²»ÊÇµÚÒ»ÐÐ£©
                        $previousSiblingTr.addClass("ct");//Ñ¡ÖÐµÄÐÐ¼Ó±³¾°
                        $this.val($previousSiblingTr.find("div:last").html());//Ñ¡ÖÐÐÐÄÚÈÝÉèÖÃµ½ÊäÈë¿òÖÐ
                        
                        //div¹ö¶¯µ½Ñ¡ÖÐµÄÐÐ,jquery-1.6.1 $$previousSiblingTr.offset().top ÓÐbug£¬ÊýÖµÓÐÎÊÌâ
                        $bigAutocompleteContent.scrollTop($previousSiblingTr[0].offsetTop - $bigAutocompleteContent.height() + $previousSiblingTr.height());
                        }else{
                            $this.val(bigAutocomplete.holdText);//ÊäÈë¿òÏÔÊ¾ÓÃ»§Ô­Ê¼ÊäÈëµÄÖµ
                            }
                    
                    break;
                    case 27://ESC¼üÒþ²ØÏÂÀ­¿ò
                    
                    bigAutocomplete.hideAutocomplete();
                    break;
                    }
            });
            
            //ÊäÈë¿òkeyupÊÂ¼þ
            $this.keyup(function(event) {
                var k = event.keyCode;
                var ctrl = event.ctrlKey;
                var isFunctionalKey = false;//°´ÏÂµÄ¼üÊÇ·ñÊÇ¹¦ÄÜ¼ü
                for(var i=0;i<bigAutocomplete.functionalKeyArray.length;i++){
                    if(k == bigAutocomplete.functionalKeyArray[i]){
                        isFunctionalKey = true;
                        break;
                        }
                    }
                //k¼üÖµ²»ÊÇ¹¦ÄÜ¼ü»òÊÇctrl+c¡¢ctrl+xÊ±²Å´¥·¢×Ô¶¯²¹È«¹¦ÄÜ
                if(!isFunctionalKey && (!ctrl || (ctrl && k == 67) || (ctrl && k == 88)) ){
                    var config = $this.data("config");
                    
                    var offset = $this.offset();
                    $bigAutocompleteContent.width(config.width);
                    var h = $this.outerHeight() - 1;
                    $bigAutocompleteContent.css({"top":offset.top + h,"left":offset.left});
                    
                    var data = config.data;
                    var url = config.url;
                    var keyword_ = $.trim($this.val());
                    if(keyword_ == null || keyword_ == ""){
                        bigAutocomplete.hideAutocomplete();
                        return;
                    }
                    if(data != null && $.isArray(data) ){
                        var data_ = new Array();
                        for(var i=0;i<data.length;i++){
                            if(data[i].title.indexOf(keyword_) > -1){
                                data_.push(data[i]);
                                }
                            }
                        
                        makeContAndShow(data_);
                        }else if(url != null && url != ""){//ajaxÇëÇóÊý¾Ý
                            $.post(url,{keyword:keyword_},function(result){
                                makeContAndShow(result.data)
                                },"json")
                            }

                    
                    bigAutocomplete.holdText = $this.val();
                    }
                //»Ø³µ¼ü
                if(k == 13){
                    var callback_ = $this.data("config").callback;
                    if($bigAutocompleteContent.css("display") != "none"){
                        if(callback_ && $.isFunction(callback_)){
                            callback_($bigAutocompleteContent.find(".ct").data("jsonData"));
                            }
                        $bigAutocompleteContent.hide();
                        }
                    }
                
            });
            
            
            //×é×°ÏÂÀ­¿òhtmlÄÚÈÝ²¢ÏÔÊ¾
            function makeContAndShow(data_){
                if(data_ == null || data_.length <=0 ){
                    return;
                    }
                
                var cont = "<table><tbody>";
                for(var i=0;i<data_.length;i++){
                    cont += "<tr><td><div>" + data_[i].title + "</div></td></tr>"
                    }
                cont += "</tbody></table>";
                $bigAutocompleteContent.html(cont);
                $bigAutocompleteContent.show();
                
                //Ã¿ÐÐtr°ó¶¨Êý¾Ý£¬·µ»Ø¸ø»Øµ÷º¯Êý
                $bigAutocompleteContent.find("tr").each(function(index){
                    $(this).data("jsonData",data_[index]);
                    })
                    }
            
            
            //ÊäÈë¿òfocusÊÂ¼þ
            $this.focus(function(){
                bigAutocomplete.currentInputText = $this;
                });
            
            }
        //Òþ²ØÏÂÀ­¿ò
        this.hideAutocomplete = function(){
            var $bigAutocompleteContent = $("#bigAutocompleteContent");
            if($bigAutocompleteContent.css("display") != "none"){
                $bigAutocompleteContent.find("tr").removeClass("ct");
                $bigAutocompleteContent.hide();
            }
            }
        
        };
    
    
    $.fn.bigAutocomplete = bigAutocomplete.autocomplete;
    
})(jQuery)
