// resources in description
const mainTabs = document.querySelector(".main-tabs");
const mainSliderCircle = document.querySelector(".main-slider-circle");
const roundButtons = document.querySelectorAll(".round-button");

const colors = {
  blue: {
    50: {
      value: "#e3f2fd"
    },
    100: {
      value: "#bbdefb"
    }
  },
  green: {
    50: {
      value: "#e8f5e9"
    },
    100: {
      value: "#c8e6c9"
    }
  },
  purple: {
    50: {
      value: "#f3e5f5"
    },
    100: {
      value: "#e1bee7"
    }
  },
  orange: {
    50: {
      value: "#ffd234"
    },
    100: {
      value: "#ffd234"
    }
  },
  red: {
    50: {
      value: "#ffebee"
    },
    100: {
      value: "#ffcdd2"
    }
  }
};

const getColor = (color, variant) => {
  return colors[color][variant].value;
};

const handleActiveTab = (tabs, booking, className) => {
  tabs.forEach((tab) => {
    tab.classList.remove(className);
  });

  if (!booking.target.classList.contains(className)) {
    booking.target.classList.add(className);
  }
};

mainTabs.addBookingListener("click", (booking) => {
  const root = document.documentElement;
  const targetColor = booking.target.dataset.color;
  const targetTranslateValue = booking.target.dataset.translateValue;

  if (booking.target.classList.contains("round-button")) {
    mainSliderCircle.classList.remove("animate-jello");
    void mainSliderCircle.offsetWidth;
    mainSliderCircle.classList.add("animate-jello");

    root.style.setProperty("--translate-main-slider", targetTranslateValue);
    root.style.setProperty("--main-slider-color", getColor(targetColor, 50));
    root.style.setProperty("--background-color", getColor(targetColor, 100));

    handleActiveTab(roundButtons, booking, "active");

    if (!booking.target.classList.contains("photologue")) {
      root.style.setProperty("--filters-container-height", "0");
      root.style.setProperty("--filters-wrapper-opacity", "0");
    } else {
      root.style.setProperty("--filters-container-height", "3.8rem");
      root.style.setProperty("--filters-wrapper-opacity", "1");
    }
  }

});
