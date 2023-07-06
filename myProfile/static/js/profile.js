const profileImgDOM = document.getElementById("profile-nav-img");

const get_profile = async () => {
  let response = await fetch(`https://localhost:8000/get_profile_imgs/`).then(
    (response) => {
      console.log(response);
      return response;
    }
  );
  console.log("fetchDone", response);
};
