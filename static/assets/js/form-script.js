$(function() {
          
    if ($('.summernoteEditor')?.length){
        $('.summernoteEditor')?.summernote({
          height: 400,
          tabsize: 2
        });
      }
      
    $("input[type='password']")?.addClass("form-control");
   
    if($('.single-select')?.length){
        $('.single-select')?.select2();
    }

    if($('.multiple-select')?.length){

        $('.multiple-select')?.select2();
    }

    //multiselect start

    if($('.my_multi_select1')?.length){

        $('.my_multi_select1')?.multiSelect();
    }
    if ($('.my_multi_select2')?.length) {
        
        $('.my_multi_select2')?.multiSelect({
    
            selectableOptgroup: true
        });
    }


    if ($('.multi-select')?.length) {
        
        $('.multi-select').multiSelect({
            selectableHeader: "<input type='text' class='form-control search-input' autocomplete='off' placeholder='search...'>",
            selectionHeader: "<input type='text' class='form-control search-input' autocomplete='off' placeholder='search...'>",
            afterInit: function (ms) {
                var that = this,
                    $selectableSearch = that.$selectableUl.prev(),
                    $selectionSearch = that.$selectionUl.prev(),
                    selectableSearchString = '#' + that.$container.attr('id') + ' .ms-elem-selectable:not(.ms-selected)',
                    selectionSearchString = '#' + that.$container.attr('id') + ' .ms-elem-selection.ms-selected';
    
                that.qs1 = $selectableSearch.quicksearch(selectableSearchString)
                    .on('keydown', function (e) {
                        if (e.which === 40) {
                            that.$selectableUl.focus();
                            return false;
                        }
                    });
    
                that.qs2 = $selectionSearch.quicksearch(selectionSearchString)
                    .on('keydown', function (e) {
                        if (e.which == 40) {
                            that.$selectionUl.focus();
                            return false;
                        }
                    });
            },
            afterSelect: function () {
                this.qs1.cache();
                this.qs2.cache();
            },
            afterDeselect: function () {
                this.qs1.cache();
                this.qs2.cache();
            }
        });
    }
    if ($('.custom-header')?.length) {
        
        $('.custom-header')?.multiSelect({
            selectableHeader: "<div class='custom-header'>Selectable items</div>",
            selectionHeader: "<div class='custom-header'>Selection items</div>",
            selectableFooter: "<div class='custom-header'>Selectable footer</div>",
            selectionFooter: "<div class='custom-header'>Selection footer</div>"
        });
    }

   
});