<template>
  <router-view />
</template>

<style lang="scss">
@import url('https://rsms.me/inter/inter.css');
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap');

:root {
  box-sizing: border-box;
}

*,
:before,
:after {
  box-sizing: inherit;
}

* {
  font-family: 'Inter', system-ui, sans-serif;
}

body {
  margin: 0;
  color: #1D1D1D;
  line-height: 1.5;
}

h1, h2, h3, h4, h5, h6 {
  line-height: 1.25;
}

h4, h5, h6 {
  color: #646978;
  font-weight: normal;
}

a {
  text-decoration: none;
  color: #0082FF;
}

.container {
  display: flex;
  flex-flow: column;
  justify-content: space-between;
  align-items: center;
  min-height: 100vh;
  width: 100%;

  & > * {
    padding: 0 15px;
    width: 100%;
    max-width: 640px;
  }

  & > .image {
    padding: 0;
    width: auto;
  }

}

input, textarea {
  background: #FBFCFF;
  border: 1px solid #ECEEF2;
  box-sizing: border-box;
  border-radius: 10px;
  padding: 16px 16px 15px;
  color: #353946;
  transition: all .15s ease-in-out;
  margin-bottom: 16px;
  width: 100%;
  font-size: 16px;

  &::placeholder {
    color: #646978;
    opacity: 0.6;
  }

  &:focus {
    outline: none;
    box-shadow: 0 0 0 4px #87abf9;
  }

  &.gosUslugi {
    padding: 0 16px;
    font-size: 18px;
    line-height: 48px;
    background: #fff;
    border: 1px solid #cdd1d4;
    color: #101010;
    border-radius: 0;

    &:focus {
      box-shadow: 0 0 0 2px #accae3;
    }
  }
}

.toggle {
  display: flex;
  justify-content: space-between;
  margin-bottom: 16px;

  & > *:first-child {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
  }

  & > *:nth-child(2):not(:last-child) {
    border-radius: 0;
  }

  & > *:last-child {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
  }

  & > * {
    background: #FBFCFF;
    color: #353946;
  }

  & > *.active {
    background: #0082FF;
    color: #FFFFFF;
  }
}

button {
  background: #0082FF;
  border-radius: 10px;
  color: #FFFFFF;
  padding: 16px 24px 17px;
  border: none;
  text-align: center;
  transition: all .15s ease-in-out;
  width: 100%;
  cursor: pointer;
  font-size: 16px;

  &:hover, &:focus {
    background: #1e90ff;
    color: #FFFFFF;
  }

  &:focus {
    outline: none;
    box-shadow: 0 0 0 4px #87abf9;
  }

  &.danger {
    background: #FFFFFF;
    border: 1px solid #FFBEBE;
    color: #FF5151;

    &:hover, &:focus {
      background: #FF5151;
      color: #FFFFFF;
    }

    &:focus {
      box-shadow: 0 0 0 4px #FFBEBE;
    }
  }

  &.gosUslugi {
    background: #FFFFFF;
    border-radius: 4px;
    border: 1px solid #565656;
    color: #565656;
    font-size: 18px;

    &:hover {
      background: #f5f5f5;
      color: #3c3c3c;
    }

    &:active {
      background: #e0e0e0;
      color: #000000;
    }

    &:focus {
      box-shadow: none;
    }

    &.blue {
      background: #0063B0;
      color: #FFFFFF;
      border: none;

      &:hover {
        background: #023E83;
        color: #FFFFFF;
      }

      &:active {
        background: #002957;
        color: #FFFFFF;
      }
    }
  }
}

.surface {
  background: #F9F9FC;
  border-radius: 16px;
  padding: 16px;
  width: 100%;
  display: flex;
  align-items: center;
  margin-bottom: 20px;
  position: relative;

  & > * + * {
    margin-left: 20px;
  }
}
</style>
