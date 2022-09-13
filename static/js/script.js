$(window).on('load', function () {
  // $(".loader-holder").delay(1000).fadeOut("slow");
  $('.loader-holder').hide()
  $('.all-content').css('display', 'block')
})

$(document).ready(function () {
  $('#currentYear').text(new Date().getFullYear())
  attachTopScroller('.scrollUp')
})

function attachTopScroller(elementId) {
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $(elementId).fadeIn()
    } else {
      $(elementId).fadeOut()
    }
  })
  // Scroll To Top Animation
  $(elementId).click(function () {
    $('html, body').animate(
      {
        scrollTop: 0,
      },
      0,
    )
    return false
  })
}

// function addCurrentNavClass() {
//   console.log(window.location.href)
// }
$(document).ready(function () {
  currentUrl = window.location.href
  relUrl = currentUrl.replace(/^(?:\/\/|[^/]+)*\//, '')
  if (relUrl === '') {
    $(`#index-link`).addClass('active')
  } else {
    $(`#${relUrl}-link`).addClass('active')
  }
})
